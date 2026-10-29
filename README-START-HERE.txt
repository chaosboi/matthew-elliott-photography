MATTHEW ELLIOTT PHOTOGRAPHY — EDITABLE VERSION

IMPORTANT: The editing interface is Pages CMS (https://pagescms.org), not a login form on the public site.

ONE-TIME SETUP
1. Create a free GitHub account if needed.
2. Create a NEW GitHub repository (e.g. matthew-photography), and upload ALL files from this extracted folder, including the hidden .pages.yml file. The .pages.yml file is essential.
3. Open https://pagescms.org and sign in with GitHub. Authorise the repository and select it. You should see 'Photographs' and 'Website text and settings'.
4. In Netlify, use 'Add new project' -> 'Import an existing project' -> GitHub. Choose the repository and deploy. The included netlify.toml runs the gallery build automatically.
5. If your existing Netlify site is already in use, instead connect THAT existing site to the GitHub repository in its build/deployment settings, rather than creating a second site. Check the new deploy before changing chaosboi.com DNS.

ONGOING EDITING
- Go to https://pagescms.org, sign in, open your repository and choose Photographs or Website text and settings.
- Add a photograph, title, gallery and order number, then save. Pages CMS commits to GitHub; Netlify redeploys automatically.
- The gallery labels are currently fixed to the six existing galleries. To add a NEW category, update .pages.yml select options and scripts/build.py categories.
- The 10 Carnies photographs are included. Other gallery photographs are clearly marked as samples; replace them with your own.
- Set a real contact email before sharing the site publicly. An empty email is currently configured.

NOTES
- Pages CMS and GitHub permissions require your own login/authorisation. The editor is not active until you finish setup.
- GitHub's repository and Netlify site can be private/public as their free plans permit; never commit secrets or private original photographs to a public repository.
- Pages CMS may have media upload size and GitHub file-size limits. Optimise JPEG/WebP photos before uploading.
- Keep this ZIP as a backup. For GitHub, upload the EXTRACTED files, not the ZIP itself.
