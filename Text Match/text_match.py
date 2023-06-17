import paddlehub

lda_news = paddlehub.Module(name="lda_news")
lda_sim = lda_news.cal_query_doc_similarity(query='航母', document='乔治·华盛顿号航母编队向钓鱼岛东以35节速度入禁航区')

print(lda_sim)