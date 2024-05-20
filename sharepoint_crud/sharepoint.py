from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.files.file import File
from office365.sharepoint.files.file_creation_information import FileCreationInformation
import os

class SharePointCrud():
    """Class for interacting with SharePoint.
    """
    def __init__(self, site, username, password):
        self._site = site
        self._username = username
        self._password = password


    @property
    def site(self):
        return self._site


    @site.setter
    def site(self, site):
        self._site = site


    @property
    def username(self):
        return self._username


    @username.setter
    def username(self, username):
        self._username = username


    @property
    def password(self):
        return self._password


    @password.setter
    def password(self, password):
        self._password = password


    def _auth(self) -> ClientContext:
        """Method for authenticating the user.

        Returns:
            ClientContext: context for the user.
        """
        conn = ClientContext(self._site).with_credentials(UserCredential(self._username, self._password))
        return conn


    def get_files_list(self, folder_name:str) -> list:
        """Method for getting the list of files in a folder.

        Args:
            folder_name (str): The name of the folder.

        Returns:
            list: List of files in the folder.
        """
        conn = self._auth()
        target_folder_url = f"{folder_name}"
        root_folder = conn.web.get_folder_by_server_relative_url(target_folder_url)
        root_folder.expand(['Files', 'Folders']).get().execute_query()
        return root_folder.files


    def get_file(self, folder_name:str, file_name:str) -> bytes:
        """Method for getting the content of a file.

        Args:
            folder_name (str): the name of the folder.
            file_name (str): the name of the file.

        Returns:
            bytes: the content of the file.
        """
        conn = self._auth()
        file_url = f'/sites/{folder_name}/{file_name}'
        file = File.open_binary(conn, file_url)
        return file.content


    def upload_file(self, file:str, folder_name:str, overwrite:bool=False) -> any:
        """Method for uploading a file to a folder.

        Args:
            file (str): the filename from the file to be uploaded.
            folder_name (str): the name of the folder on SharePoint.
            overwrite (bool, optional): whether to overwrite the file if it already exists. Defaults to False.

        Returns:
            any: the response from the server.
        """
        conn = self._auth()
        target_folder_url = f'/sites/{folder_name}'
        file_info = FileCreationInformation()
        file_info.content = open(file, 'rb').read()
        file_info.url = os.path.basename(file)
        file_info.overwrite = overwrite
        target_folder = conn.web.get_folder_by_server_relative_url(target_folder_url)
        response = target_folder.files.add(file_info).execute_query()
        return response
