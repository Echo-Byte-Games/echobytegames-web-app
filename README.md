# Echo Byte Games — website

A retro pixel-arcade style static website for **Echo Byte Games**, ready to deploy on **Firebase Hosting**.

## Pages

| File | URL (local) | Description |
| --- | --- | --- |
| `public/index.html` | `/` | Home / hero / featured games |
| `public/games.html` | `/games` | Game catalogue |
| `public/about.html` | `/about` | About the studio |
| `public/privacy.html` | `/privacy` | Privacy policy |
| `public/contact.html` | `/contact` | Contact form + email |
| `public/404.html` | any missing route | Game-over error page |

## Project structure

```
.
├── firebase.json          # Firebase Hosting configuration
├── .firebaserc            # Firebase project alias (set your project ID)
├── public/                # The folder Firebase deploys
│   ├── css/style.css
│   ├── js/main.js
│   ├── images/            # Generated pixel-art SVGs
│   └── *.html
└── tools/gen_art.py       # Regenerates the pixel-art SVGs
```

## Run locally

No build step or dependencies are needed. Open `public/index.html` in a browser, or serve the folder:

```bash
# From the project root (Python 3)
python -m http.server 5000 --directory public
```

Then visit http://localhost:5000

To preview exactly how Firebase will serve it (including clean URLs):

```bash
firebase emulators:start --only hosting
```

## Deploy to Firebase Hosting

1. Install the Firebase CLI (requires Node.js):

   ```bash
   npm install -g firebase-tools
   ```

2. Log in:

   ```bash
   firebase login
   ```

3. Create a Firebase project in the [Firebase console](https://console.firebase.google.com/) if you don't have one yet.

4. Tell the CLI which project to use — either replace `YOUR-FIREBASE-PROJECT-ID` in `.firebaserc`, or run:

   ```bash
   firebase use --add
   ```

5. Deploy:

   ```bash
   firebase deploy --only hosting
   ```

Firebase will print your live Hosting URL (e.g. `https://your-project.web.app`).

### Custom domain

In the Firebase console, go to **Hosting → Add custom domain** and follow the DNS instructions.

## Customising the site

- **Games:** edit the cards in `public/games.html` and the featured cards on `public/index.html`. The four games included (NEON DRIFT, DUNGEON BITS, STARFALL, PIXEL PUZZLE) are placeholders — swap the titles, descriptions and thumbnails in `public/images/` for your real games.
- **Email address:** update `EMAIL` in `public/js/main.js` and the visible address in `public/contact.html` / `public/privacy.html`.
- **Privacy policy:** the full text lives in `public/privacy.html`.
- **Colours / fonts:** edit the variables at the top of `public/css/style.css`.
- **Pixel art:** change the bitmaps in `tools/gen_art.py` and run `python tools/gen_art.py` to rebuild the SVGs in `public/images/`.

> Note: the contact form opens the visitor's email app with a pre-filled message (there is no server-side form handler). If you want messages submitted directly to an inbox, connect a service such as Formspree or Firebase Functions/Email Extension later.
