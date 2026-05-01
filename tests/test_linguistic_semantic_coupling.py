from memory import IdentityField, SemanticMemory, EpisodicMemory, analyze_linguistic_coupling


def _episode(content, t, phase=0.5, salience=0.85, impact=0.85):
    episodic = EpisodicMemory()
    episodic.store(content, {
        'timestamp': float(t),
        'salience': salience,
        'identity_impact': impact,
    })
    ep = episodic.episodes[-1]
    ep.phase_at_storage = phase
    return ep


def test_linguistic_profile_prefers_complete_sentence_over_fragment():
    key = 'adrian prefers rigor'
    sentence = analyze_linguistic_coupling('Adrian prefers rigor.', key)
    fragment = analyze_linguistic_coupling('rigor', key)

    assert sentence.grammaticality > fragment.grammaticality
    assert sentence.coupling >= fragment.coupling
    assert sentence.profile.token_count > fragment.profile.token_count


def test_semantic_memory_records_linguistic_coupling_on_trace():
    identity = IdentityField(initial_phase=0.5)
    m3 = SemanticMemory(identity)

    trace = m3.observe_episode(_episode('Adrian prefers rigor.', 0, phase=0.51))

    assert 0.0 <= trace.grammar_score <= 1.0
    assert 0.0 <= trace.semantic_anchor_score <= 1.0
    assert 0.0 <= trace.linguistic_coupling <= 1.0
    assert trace.linguistic_coupling > 0.0


def test_semantic_memory_retrieval_exposes_language_fit():
    identity = IdentityField(initial_phase=0.5)
    m3 = SemanticMemory(identity)

    for i in range(3):
        m3.observe_episode(_episode('Adrian prefers rigor.', i, phase=0.50 + 0.01 * i))
    m3.check_semantic_candidate_creation('adrian prefers rigor')
    item = m3.consolidate_candidate('adrian prefers rigor', 10.0)
    assert item is not None

    results = m3.retrieve('Adrian prefers rigor?', identity, top_k=1)
    assert results
    assert 'language_fit' in results[0]
    assert 'query_grammar' in results[0]
    assert results[0]['language_fit'] >= 0.0
