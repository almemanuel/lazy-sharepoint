from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.files.file import File

class SharePointCrud():
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


    def _auth(self):
        conn = ClientContext(self._site).with_credentials(UserCredential(self._username, self._password))
        return conn


    def get_files_list(self, folder_name):
        conn = self._auth()
        target_folder_url = f"{folder_name}"
        root_folder = conn.web.get_folder_by_server_relative_url(target_folder_url)
        root_folder.expand(['Files', 'Folders']).get().execute_query()
        return root_folder.files


    def get_file(self, folder_name, file_name):
        conn = self._auth()
        file_url = f'/sites/{folder_name}/{file_name}'
        file = File.open_binary(conn, file_url)
        return file.content
