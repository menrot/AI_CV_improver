FIXED_KEYS = ['NAME','SUMMARY','DOB','WORKING AS','CONTACTS']VARIABLE_KEYS = ['EXPERIENCE','SCHOOL']ORDERED_KEYS = ['NAME','DOB','WORKING AS','SUMMARY','EXPERIENCE','SCHOOL','CONTACTS']DOB_PROMPT = 'Check that the following date is in YYYY/MM/DD. Correct it if its not in the same format, otherwise return the same: 'SUMMARY_PROMPT_CONVERT = 'Convert the text in a CV summary:'TEMPERATURE_SUMMARY_PROMPT_CONVERT = 0.8SUMMARY_PROMPT_IMPROVER = 'Improve the following text quality:'TEMPERATURE_SUMMARY_PROMPT_IMPROVER = 0.3OPENAIMODEL = 'text-davinci-003'OPENAIKEY = "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"TEMPLATE_FILE = 'cv_template.txt'EXPERIENCE_PROMPT_CONVERT = "Make the text more appealing for a recruiter:"RESULT_FILE = 'cv_improved.txt'