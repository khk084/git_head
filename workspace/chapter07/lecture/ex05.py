from re import findall, sub
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A123&***$?']

texts_re1 = [t.lower() for t in texts]
texts_re2 = [sub('[0-9]', '', text) for text in texts_re1]
texts_re3 = [sub('[&.,?$;:*]', '', text) for text in texts_re2]
texts_re4 = [sub(' ', '', text) for text in texts_re3]
print(texts_re4)