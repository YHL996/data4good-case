Project title: USING LARGE LANGUAGE MODELS FOR ENTITY EXTRACTION IN THE HEALTHCARE SECTOR (DATA4GOOD Competition https://business.purdue.edu/events/data4good/)

In this project, our team leveraged the Mistral OpenOrca 7B model to enhance data extraction accuracy significantly, aligning our results closely with the intended problem statements. Key improvements included capitalizing brand-named drugs, accurately imputing ages, and refining spacing and grammar, which collectively reduced the Word Error Rate (WER) to 0.53738 on test data, closely mirroring the ideal solution. This precision was pivotal in securing 4th place among 95 teams in a private Kaggle competition.

Open-source models, while beneficial for secure hosting on private servers, face limitations in language translation and API rate restrictions. Addressing these challenges is essential for achieving higher extraction accuracies. Our development process involved choosing openrouter.ai for its efficient open-source model endpoints, allowing seamless integration into our code. This included multiple adjustments to the prompt template for optimal Named Entity Recognition (NER) outputs.

The post-processing phase was critical, involving error corrections, model chaining, and data cleaning, particularly using regression for missing values, which collectively contributed to the reduced WER. We benchmarked our process against Kaggle competition submissions and employed A/B testing for iterative improvements. Manual comparisons with human transcription results provided valuable insights, further guiding code post-processing for accuracy.

In the healthcare sector, where there is a shortage of physicians (2.47 per 1000 people), automating decision processes with open-source large language models can streamline operations, ensure content accuracy, and enhance HIPAA compliance. Our study, analyzing 2001 artificial transcripts from a Kaggle competition, demonstrated that utilizing AI can significantly optimize data processing and administrative tasks while maintaining regulatory compliance.

A poster about this project can be found here: https://github.com/YHL996/data4good-case/blob/main/Mini%20Poster.pdf
