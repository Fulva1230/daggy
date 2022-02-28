import requests as r
res = r.get("https://api.github.com/repos/gohugoio/hugo/releases/latest")

# %%
json_response = res.json()
# %%
hugo_deb_pack_info = next(filter(lambda asset: "64bit.deb" in asset["name"] and "hugo_extended" in asset["name"], json_response["assets"]))
#%%
hugo_deb_pack_file_response = r.get(hugo_deb_pack_info["browser_download_url"], stream=True)
with open("hugo.deb", 'wb') as fd:
    for chunk in hugo_deb_pack_file_response.iter_content(chunk_size=128):
        fd.write(chunk)
