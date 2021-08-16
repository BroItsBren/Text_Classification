import nltk 

text = nltk.word_tokenize("A discipline that focuses on ensuring that only approved roles are able to create, read, update, or delete data – and only using appropriate and controlled methods. Data Governance programs often focus on supporting Access Management by aligning the requirements and constraints posed by  Governance, Risk Management, Compliance, Security, and Privacy efforts.")
tagged_text=nltk.pos_tag(text)
print(tagged_text)

#nltk.help.upenn_tagset('NN')
#nltk.help.upenn_tagset('IN')
#nltk.help.upenn_tagset('DT')