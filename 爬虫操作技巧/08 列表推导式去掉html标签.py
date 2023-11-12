original_list = ['\n凿破苍苔涨作池，芰荷分得绿参差。<br />晓开一朵烟波上，似画真妃出浴时']
cleaned_list = [item.replace('\n', '').replace('<br />', '') for item in original_list]
print(cleaned_list)

