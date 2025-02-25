import logging
from app.aws.config import s3, s3_resource

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class S3Service:
    def __init__(self):
        # Initialize the S3 client and resource for AWS operations
        self.s3_client = s3
        self.s3_resource = s3_resource

    async def upload_file(self, file, bucket_name, folder_name, file_name):
        """
        Uploads a file to an S3 bucket.
        - `file`: The file object to upload.
        - `bucket_name`: The name of the S3 bucket.
        - `folder_name`: The folder in the bucket where the file will be stored.
        - `file_name`: The name of the file in the bucket.
        Returns `True` if successful, otherwise `False`.
        """
        try:
            key = f"{folder_name}/{file_name}"  # Construct the file key (path)
            self.s3_client.upload_fileobj(file, bucket_name, key)  # Upload the file
            return True
        except Exception as ex:
            logger.error(f"Unexpected Error: {ex}")  # Log errors
            return False

    async def get_all_files(self, bucket_name):
        """
        Retrieves a list of all files in an S3 bucket.
        - `bucket_name`: The name of the S3 bucket.
        Returns the list of files if successful, otherwise `False`.
        """
        try:
            files = self.s3_client.list_objects_v2(Bucket=bucket_name)  # List objects in the bucket
            return files
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")  # Log errors
            return False

    def download_file(self, file_name: str, bucket_name: str):
        """
        Generates a pre-signed URL to download a file from an S3 bucket.
        - `file_name`: The key (path) of the file in the bucket.
        - `bucket_name`: The name of the S3 bucket.
        Returns the pre-signed URL if successful, otherwise raises an exception.
        """
        try:
            url = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': bucket_name, 'Key': file_name},  # Generate URL with expiration
                ExpiresIn=3600  # URL expires in 1 hour
            )
            return url
        except Exception as ex:
            logger.error(f"Unexpected Error: {ex}")  # Log errors
            raise ex()

    async def delete_file(self, bucket_name: str, file_key: str):
        """
        Deletes a file from an S3 bucket.
        - `bucket_name`: The name of the S3 bucket.
        - `file_key`: The key (path) of the file to delete.
        Returns `True` if successful, otherwise `False`.
        """
        try:
            self.s3_client.delete_object(Bucket=bucket_name, Key=file_key)  # Delete the file
            logger.info(f"File {file_key} deleted successfully from bucket {bucket_name}.")  # Log success
            return True
        except Exception as ex:
            logger.error(f"Error deleting file {file_key} from bucket {bucket_name}: {ex}")  # Log errors
            return False