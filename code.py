import pandas as pd
df = pd.read_csv('submission_last.csv')
# df = df[:185441]
df = df.drop_duplicates(['key_id'])
df.to_csv('submission_AST.csv', index=False)
