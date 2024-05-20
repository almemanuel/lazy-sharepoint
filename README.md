# sharepoint-crud

![GitHub repo size](https://img.shields.io/github/repo-size/almemanuel/sharepoint-crud?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/almemanuel/sharepoint-crud?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/almemanuel/sharepoint-crud?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/almemanuel/sharepoint-crud?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/almemanuel/sharepoint-crud?style=for-the-badge)


> Solution to integrate SharePoint with your Python script

### Improvement

This project is under development, so if you have any suggestions, please let me know:

- [x] Get file content
- [ ] Search for a file
- [x] Upload file
- [ ] Edit file
- [ ] Delete a file

## 💻 Requeriments
Before you begin, ensure you have met the following requirements:
- you have installed a `python 3.8` or higher

## 🚀 Install sharepoint-crud
- run the command: `pip install sharepoint-crud` to activate the virtual environment
- voilà!

## ☕ Run
To run sharepoint-crud, you need a sharepoint account. You can instanciate an object with the following parameters:

```python
from sharepoint-crud import SharePointCrud

sharepoint = SharePointCrud(
  'https://your-site.sharepoint.com/sites/your-library',
  'your-email@your-domain.com',
  'your-password'
)

```

Actually, is possible download and upload file. An example:

```python
file_content = sharepoint.get_file('your/folder/to/your/file', 'your-file.file_format')

```
An example:
I have a file `example.csv` in the folder `my_library/Shared Files/my_folder` on SharePoint:
```python
from sharepoint-crud import SharePointCrud

file_content = SharePointCrud(
  'https://your-site.sharepoint.com/sites/your-library',
  'your-email@your-domain.com',
  'your-password'
).get_file('my_library/Shared Files/my_folder', 'example.csv')
```

## 📫 Contributing

To contribute to sharepoint-crud, follow these steps:
1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and confirm them: `git commit -m '<commit_message>'`
4. Send to the original branch: `git push origin <project_name> <location>`
5. Create the pull request.

Alternatively, consult the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 🤝 Colaborators

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/almemanuel" title="Emanuel's GitHub">
        <img src="https://avatars.githubusercontent.com/u/40006289?v=4" width="100px;" alt="Emanuel's profile photo"/><br>
        <sub>
          <b>Emanuel Almeida</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## 📝 Licença

This project is under license. See the file [LICENÇA](LICENSE.md) for more details.

[⬆ Turn to top](#sharepoint-crud)
<br>
