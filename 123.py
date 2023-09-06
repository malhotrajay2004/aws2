import boto3

def get_csv_to_s3(bucket_name, s3_key, file_name):
	s3 = boto3. client ('s3')
	try:
		s3.download_file(bucket_name, s3_key, file_name)
		print ("File download successfully to S3")
	except Exception as e:
		print (f"An error occurred: {str(e)}")

bucket_name = 'jay69'// "Hone apna apna hi likha hai"
file_name = 'data.csv'// "ye target file hai jo download Kardenge"
s3_key = 'raw.csv'// "ye source file hai jisko download Kar dense"

get_csv_to_s3(bucket_name, s3_key, file_name)