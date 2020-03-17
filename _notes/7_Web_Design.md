# 7. Web Design

## 19 Intro to Tailwind CSS

### What is Gulp?

- SCSS -> ugly CSS
- New JavaScript -> Old JavaScript
- Pug.js -> ugly HTML
- uploading to github automization

### [Check gulp project for details of dependencies](https://github.com/snoop2head/gulp-gulp-gulp)

```shell
npm init
npm install gulp gulp-postcss gulp-sass gulp-csso node-sass auto-prefixer -D
npm install tailwindcss -D
```

- If you don't do npm init, then node modules will be installed in upper directory with npm on it
- initialize tailwind css

```shell
npx tailwindcss init
```

### Compile scss to css

- make alias on package.json

  ```json
  "scripts": {
      "css": "gulp"
    }
  ```

- compile scss into css file

  ```shell
  npm run css
  ```



## 20 Design



