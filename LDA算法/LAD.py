import paddlehub

lda_news = paddlehub.Module(name="lda_news")
#jsd, hd = lda_news.cal_doc_distance(doc_text1="今天的天气如何，适合出去游玩吗", doc_text2="感觉今天的天气不错，可以出去玩一玩了")
# jsd = 0.003109, hd = 0.0573171

lda_sim = lda_news.cal_query_doc_similarity(query='百度搜索引擎', document='百度是全球最大的中文搜索引擎、致力于让网民更便捷地获取信息，找到所求。百度超过千亿的中文网页数据库，可以瞬间找到相关的搜索结果。')
# LDA similarity = 0.06826
print(lda_sim)
results = lda_news.cal_doc_keywords_similarity('百度是全球最大的中文搜索引擎、致力于让网民更便捷地获取信息，找到所求。百度超过千亿的中文网页数据库，可以瞬间找到相关的搜索结果。')
# [{'word': '百度', 'similarity': 0.12943492762349573},
#  {'word': '信息', 'similarity': 0.06139783578769882},
#  {'word': '找到', 'similarity': 0.055296603463188265},
#  {'word': '搜索', 'similarity': 0.04270794098349327},
#  {'word': '全球', 'similarity': 0.03773627056367886},
#  {'word': '超过', 'similarity': 0.03478658388202199},
#  {'word': '相关', 'similarity': 0.026295857219683725},
#  {'word': '获取', 'similarity': 0.021313585287833996},
#  {'word': '中文', 'similarity': 0.020187103312009513},
#  {'word': '搜索引擎', 'similarity': 0.007092890537169911}]
