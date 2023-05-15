import feed_me


texts = [feed_me.FeedMeItem(
    text="Paragraph 1",
    source= "http://1.com/"
),
feed_me.FeedMeItem(
    text="Paragraph 2",
    source= "http://2.com/"
),
feed_me.FeedMeItem(
    text="Paragraph 3",
    source= "http://3.com/"
)]
feed_me.show(texts)
