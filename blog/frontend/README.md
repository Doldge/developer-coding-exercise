# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.


# Notes From the Author

I wasn't sure what the "correct" way to have react play nice with django was given that they're running on separate ports, and are thus treated as separate domains [CORS] by the browser. What I've ended up doing is pointing the django `static` directory at the `builds/static` directory in the react app. I've also created a sym-link from `templates/index.html` to the `builds/index.html`.

To run the app then, you need to:
```bash

yarn build
./run_django.sh
# then navigate to the root of the django app.
```

*This means the react app will only work with `yarn build`, and likely only on unix machines.*

Would correct this if I knew how.
