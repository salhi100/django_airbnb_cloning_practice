const gulp = require("gulp");

const css = () => {
  const postCSS = require("gulp-postcss");
  const sass = require("gulp-sass");
  const minifyCSS = require("gulp-csso");
  sass.compiler = require("node-sass");
  return gulp
    .src("assets/scss/styles.scss")
    .pipe(sass().on("error", sass.logError))
    .pipe(postCSS([require("tailwindcss"), require("autoprefixer")]))
    .pipe(minifyCSS())
    .pipe(gulp.dest("static/css"));
};

exports.default = css;
