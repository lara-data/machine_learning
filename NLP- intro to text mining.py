#!/usr/bin/env python
# coding: utf-8

# In[70]:


from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# In[47]:


text = "It was always likely that the months of lockdown would demand some kind of emotional catharsis. You imagined it would involve the usual British excesses of lager and sunshine. In fact, in the past week its primary expression has been a coming together of mostly young people in our cities under the banner of Black Lives Matter. On Saturday, in by far the largest of the week’s demonstrations in London, many thousands crammed shoulder to shoulder in Parliament Square in the blustery rain and edged their way forwards toward St James’s Park. On Friday, police and government ministers had warned that such a crowd was not only unlawful but certainly dangerous with the virus still being transmitted from person to person. In the midst of that crowd – an unnatural human feeling in itself for all those who have been in isolation – it was impossible not to feel that those warnings should have been heeded far more closely. But for the vast majority of those that came, the risk had seemed worth it. Some of the banners in Parliament Square made their argument succinctly: “Racism has always been a pandemic.” As well as looking like the premature end of a shutdown spring in the capital, the protest also felt very much like the beginning of something; not a one-off outpouring of rage against the brutal killing of George Floyd in Minneapolis 12 days ago, but a sustainable expression of the need for change. There was an urgency about that demand, as well as a weariness. Innumerable wounds have been opened by the graphic video of Floyd’s death, stretching back in British memories over generations – the protesters’ banners were a roll call of past and current injustice. Actor John Boyega’s heartfelt speech to the demonstrators on Wednesday made those links explicit: “We are a physical representation of our support for George Floyd … We are a physical representation of our support for Stephen Lawrence.” His words were carried on many of the cardboard signs held aloft: “Now is the time. I ain’t waiting.” That sentiment, which has spread through cities across the world, was never likely to be postponed by demands for physical distancing. The loose network of Black Lives Matter activists who have coordinated last week’s protests across the UK did their best to mitigate the risks in the crowd. They came equipped here with stocks of free masks and sanitiser. Imarn Ayton, 29, one of those coordinators, kicked off proceedings through a loudhailer: “We are not here for violence. If you commit violence today you are not for the cause. I don’t want to see no alcohol. I don’t want to see no weed. This is not a carnival. And keep your distance. You don’t need me to say that coronavirus is killing black people.” For many hours her hopes for a peaceful protest were realised, but in late afternoon there were clashes between protesters and police and one officer appeared to be knocked off their horse, which then bolted – sending crowds of people scattering. When I spoke to Ayton, 29, she said they had expected 20,000 to come. The eventual number appeared several times greater. What was not in doubt was that last week had marked a new phase of momentum in a long campaign. “I’ve always been involved,” she said of a movement that has its genesis in the protest against the decision not to prosecute the killer of Trayvon Martin in 2013. “To be honest anyone who is black and passionate is involved. But it feels like a different moment. The death of George Floyd and the protest has inspired many more people to speak up, black, white, everyone. The difference we are seeing is people are no longer prepared to be ignorant; they want to educate themselves.” A lot of the people I spoke to suggested that this was their first march. They acknowledged the risks of the crowd, but felt they had no real choice. A young black woman from north London, who didn’t wish to give her name was holding a sign saying “Your silence is violence” and sitting at the foot of Gandhi’s statue. “The facts haven’t changed,” she said, “but the difference is more people are listening. I see it on social media, everyone that I know has been posting about this. And if you are young and you are not speaking up now, then it definitely says who you are. They don’t have to be here physically because we are in the middle of a pandemic, but if they are not here mentally and in spirit, well fuck ’em.” Terence Niemi, 28, from Colchester was also a first-time protester. “I felt like I should be here, there was no real choice this time. But it shouldn’t take losing another person’s life for us to form together. Hopefully in the future we can make these kind of movements without this situation going down.” Da Vinci, a DJ from Brixton, said: “Asking people ‘stop oppressing us’ doesn’t really make much sense to me. But when you see people coming out together all around the world hopefully we can unite around that and find something positive out of it.” Fatima Abdulrahman had been on two previous protests last week. “You only have to look at the images on the internet to know why people are enraged,” she said. “There is a lot of anger; people are not OK with how things are and there is a lot of pain to process.” She suggested the grimness of the last few weeks has also motivated that change; isolation itself has sharpened the issues. “People have been at home, often alone for several months hearing about people dying, and a disproportionate number of them have been black people. And a disproportionate amount of black people have been suffering economically. That is another reason why we are here.” The summer looks likely to pitch those demands for social justice squarely against public health. The first test of that clash will be on Sunday afternoon when marchers have been invited to reassemble outside the US embassy in Vauxhall."


# In[48]:


tokSent_text = sent_tokenize(text)
tokSent_text


# In[49]:


tokWord_text = word_tokenize(text)
tokWord_text


# In[50]:


freq_w = FreqDist(tokWord_text)
freq_w


# In[51]:


most_freq = FreqDist(dict(freq_w.most_common()[:35]))
most_freq.plot()


# In[52]:


stop_words = set(stopwords.words("english"))
print(stop_words)


# In[54]:


filtered_sentence = []

for w in tokWord_text:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)


# In[57]:


freq_w2 = FreqDist(filtered_sentence)
freq_w2


# In[59]:


most_freq = FreqDist(dict(freq_w2.most_common()[:35]))
most_freq.plot()


# In[85]:


ps = PorterStemmer()

for w in filtered_sentence:
    print(ps.stem(w))


# In[88]:


filtered_text = "It alway like month lockdown would demand kind emot catharsi . you imagin would involv usual british excess lager sunshin . In fact , past week primari express come togeth mostli young peopl citi banner black live matter . On saturday , far largest week ’ demonstr london , mani thousand cram shoulder shoulder parliament squar blusteri rain edg way forward toward St jame ’ park . On friday , polic govern minist warn crowd unlaw certainli danger viru still transmit person person . In midst crowd – unnatur human feel isol – imposs feel warn heed far close . but vast major came , risk seem worth . some banner parliament squar made argument succinctli : “ racism alway pandemic. ” As well look like prematur end shutdown spring capit , protest also felt much like begin someth one-off outpour rage brutal kill georg floyd minneapoli 12 day ago , sustain express need chang . there urgenc demand , well weari . innumer wound open graphic video floyd ’ death , stretch back british memori gener – protest ’ banner roll call past current injustic . actor john boyega ’ heartfelt speech demonstr wednesday made link explicit : “ We physic represent support georg floyd … We physic represent support stephen lawrence. ” hi word carri mani cardboard sign held aloft : “ now time . I ’ waiting. ” that sentiment , spread citi across world , never like postpon demand physic distanc . the loos network black live matter activist coordin last week ’ protest across UK best mitig risk crowd . they came equip stock free mask sanitis . imarn ayton , 29 , one coordin , kick proceed loudhail : “ We violenc . If commit violenc today caus . I ’ want see alcohol . I ’ want see weed . thi carniv . and keep distanc . you ’ need say coronaviru kill black people. ” for mani hour hope peac protest realis , late afternoon clash protest polic one offic appear knock hors , bolt – send crowd peopl scatter . when I spoke ayton , 29 , said expect 20,000 come . the eventu number appear sever time greater . what  doubt last week mark new phase momentum long campaign . “ I ’ alway involv , ” said movement genesi protest decis prosecut killer trayvon martin 2013 . “ To honest anyon black passion involv . but feel like differ moment . the death georg floyd protest inspir mani peopl speak , black , white , everyon . the differ see peopl longer prepar ignor ; want educ themselves. ” A lot peopl I spoke suggest first march .  hey acknowledg risk crowd , felt real choic . A young black woman north london , ’ wish give name hold sign say “ your silenc violenc ” sit foot gandhi ’ statu . “ the fact ’ chang , ” said , “ differ peopl listen . I see social media , everyon I know post . and young speak , definit say . they ’ physic middl pandem , mental spirit , well fuck ’ em. ” terenc niemi , , colchest also first-tim protest . “ I felt like I , real choic time . but ’ take lose anoth person ’ life us form togeth . hope futur make kind movement without situat go down. ” Da vinci , DJ brixton , said : “ ask peopl ‘ stop oppress us ’ ’ realli make much sens . but see peopl come togeth around world hope unit around find someth posit it. ” fatima abdulrahman two previou protest last week . “ you look imag internet know peopl enrag , ” said . “ there lot anger ; peopl OK thing lot pain process. ” she suggest grim last week also motiv chang ; isol sharpen issu . “peopl home , often alon sever month hear peopl die , disproportion number black peopl . and disproportion amount black peopl suffer econom . that anoth reason here. ” the summer look like pitch demand social justic squar public health . the first test clash sunday afternoon marcher invit reassembl outsid US embassi vauxhal."


# In[89]:


tokenized_text = word_tokenize(filtered_text)
tokenized_text


# In[90]:


freq_w3 = FreqDist(filtered_sentence)
freq_w3


# In[91]:


most_freq = FreqDist(dict(freq_w3.most_common()[:35]))
most_freq.plot()


# In[95]:


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

wc = WordCloud(background_color="white", max_words=200, width=400, height=400, random_state=1).generate(filtered_text)
# to recolour the image
plt.imshow(wc)


# In[ ]:




