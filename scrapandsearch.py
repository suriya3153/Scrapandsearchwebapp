import streamlit as st

def main_page():
    st.markdown("# Scrap")
    st.sidebar.markdown("# Scrap 🎈")
    st.write("suriya")
    import pandas as pd
    import re
    import pymongo
    client = pymongo.MongoClient("mongodb+srv://suriya315:12345678s@cluster0.kbh9v.mongodb.net/?retryWrites=true&w=majority")
    db = client.twits
    pc=db.vals
    import snscrape.modules.twitter as sntwitter
    import pandas as pd
    
    # Creating list to append tweet data to
    tweets_list2 = []
    hashtag=st.text_input("Scrap")
    if len(hashtag)!=0:
        import datetime as date
        day=date.datetime.today()
        dateend=day.strftime("%Y-%m-%d")
        datestart="2022-10-15"
        # Using TwitterSearchScraper to scrape data and append tweets to list
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{hashtag} since:{datestart} until:{dateend}').get_items()):
            if i>100:
                break
            tweets_list2.append([tweet.date,tweet.lang, tweet.id, tweet.content,tweet.url,hashtag])
            appendlis=[{'Datetime':tweet.date,"lang":tweet.lang, 'Tweet Id':tweet.id, 'Text':tweet.content,"url":tweet.url,"hastag":hashtag}]
            pc.insert_many(appendlis)
        # Creating a dataframe from the tweets list above
        tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime',"lang", 'Tweet Id', 'Text',"url","hastag"])
        st.write(tweets_df2)

def page2():
    st.markdown("# search ❄️")
    st.sidebar.markdown("# search ❄️")
    import pandas as pd
    import re
    import pymongo
    client = pymongo.MongoClient("mongodb+srv://suriya315:12345678s@cluster0.kbh9v.mongodb.net/?retryWrites=true&w=majority")
    db = client.twits
    pc=db.vals
    import snscrape.modules.twitter as sntwitter
    import pandas as pd
    ent=st.text_input("search your content")
    if len(ent)!=0:
        g={"hastag":{"$regex":ent}}
        a=pc.find(g)
        df=pd.DataFrame(a,columns=['Datetime', "lang",'Tweet Id', 'Text',"url","hastag"])
        def textsize(x):
            if len(x)<y:
                return True
            else:
                return False
        y=st.text_input("size of tweets")
        try:
            y=int(y)
            x=df.Text.apply(textsize)
            ds=df[x]
            st.write(ds)
        except:
            st.write(df)
        


page_names_to_funcs = {
    "scrap": main_page,
    "search": page2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
