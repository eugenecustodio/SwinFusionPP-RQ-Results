import json,re,sys
cur=open(sys.argv[1]).read()
d=re.sub(r'\[([^\]]*)\]\(([^()]|\([^)]*\))*\)', lambda m: m.group(1), cur)
d=d.replace('***','').replace('**',''); d=re.sub(r'\*+','',d); d=re.sub(r'\\([\[\]\(\)\*_#+\-.!<>|~])', r'\1', d)
Q='\u2019'; NB='\u2011'
E=[
('1-email','G-Mail account (for deduplication / one submission per respondent)','UE institutional email address (for deduplication / one submission per respondent)'),
('3-fixed','to the type of video being checked (Table III).','to the type of video being checked (Table III). All four detectors used the fixed-recipe SwinFusion++ configuration described under Training Regimens and Hyperparameter Optimization, with one model trained on each benchmark dataset.'),
('5-cronbach',f'Where appropriate for instrument quality, internal consistency reliability (e.g., Cronbach{Q}s alpha by dimension) may be computed to assess whether items within a dimension behave coherently.\n',''),
('5-limitation','the built-in sample clips were all deepfakes. Security is rated','the built-in sample clips were all deepfakes. The end-user questionnaire was adapted from Urera and Balahadia (2019) and the expert questionnaire was developed for this study, and the internal consistency of neither was assessed. Security is rated'),
('T-expertdims',f'learnability, task flow clarity, feedback quality, error prevention/recovery, interpretability, consistency, transparency/help, and context{NB}of{NB}use readiness','learnability, task flow, system feedback, error prevention, error handling and recovery, language/microcopy clarity, results interpretability, consistency and standards, help/documentation/transparency, and context-of-use readiness'),
('T-inference','analyzed every frame in which the tracked face appeared by dividing the video into short clips at the frame spacing','analyzed the whole span in which the tracked face appeared by dividing it into short clips sampled at the frame spacing'),
('T-ch2output','(a) a classification label (Real/Fake), (b) a confidence score (probabilistic output associated with the predicted class), and (c) contextual video metadata',f'(a) a verdict label (Likely Deepfake or Likely Real), (b) a confidence value expressing how far the video{Q}s score falls from the detector{Q}s decision threshold, and (c) contextual video metadata'),
('T-ch1scope','including a classification label (Real/Fake), confidence score, and contextual metadata','including a verdict label (Likely Deepfake or Likely Real), a confidence value, and contextual metadata'),
('T-ch1lim','The platform produces a probabilistic classification output (Real/Fake with confidence and metadata).','The platform produces a classification output (Likely Deepfake or Likely Real, with a confidence value and metadata).'),
('T-pytorch','(Python with deep-learning frameworks such as PyTorch/TensorFlow and supporting libraries)','(Python with the PyTorch deep-learning framework and supporting libraries)'),
('T-logit','produces a clip-level fake probability and aggregates clip-level outputs into a single video-level classification','produces a clip-level score (logit), averages the clip scores of each video, and compares the video score with the frozen decision threshold to produce a single video-level classification'),
('T-deletion','; where feasible, the system deletes uploads immediately after processing.','; the system deletes each upload as soon as the check finishes.'),
('T-tense','Within this protocol, a model will be interpreted as strong only if','Within this protocol, a model is interpreted as strong only if'),
('T-grammar','Participant receive:','Participants receive:'),
('T-margin','had an estimated margin of error of \u00b10.30 scale points at a 95% confidence level','would have an estimated margin of error of \u00b10.30 scale points at a 95% confidence level under random sampling'),
]
ok=True
for i,o,n in E:
    c=d.count(o); print(f'{i:14s} {c}'); ok&=(c==1)
print('ALL UNIQUE' if ok else 'PROBLEM')
json.dump([{"replaceAllText":{"containsText":{"text":o,"matchCase":True},"replaceText":n,"tabsCriteria":{"tabIds":["t.l5c18frq5wuo"]}}} for _,o,n in E],open(sys.argv[2],'w'),ensure_ascii=True)
