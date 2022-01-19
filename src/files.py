import requests
import zipfile
import os

def download_gabarito(ano: int, fase: int, nivel: int, nome: str) -> dict:
  file = f'./{ano}f{fase}p{nivel}_{nome}.zip'
  url = f'https://olimpiada.ic.unicamp.br/static/extras/obi{ano}/gabaritos/{file}'

  r = requests.get(url, allow_redirects=True)

  if r.status_code == 200:
    open(file, 'wb').write(r.content)

    with zipfile.ZipFile(file, 'r') as zip_ref:
      zip_ref.extractall('./')

    os.remove(file)

    folder_path = file.strip('.zip')

  else:
    return {'status': r.status_code, 'content': {}}

  return {'status': r.status_code, 'content': {'folder_path': nome}}

