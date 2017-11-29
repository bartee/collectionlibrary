var gulp = require('gulp'),
    plugins = require('gulp-load-plugins')(),
    webpack = require('webpack'),
    webpackstream = require('webpack-stream'),
    del = require('del'),
    jshint = require('jshint'),
    materialize = require('materialize-css'),
    minimist = require('minimist');

var src = {
    root: 'src/',
    scss: 'src/scss/',
    img: 'src/img/',
    json: 'src/json/',
    css: 'src/css/',
    fonts: 'src/fonts/',
    js: 'src/js/'
};

var target = {
    root: 'dist/',
    scss: 'dist/scss/',
    img: 'dist/img/',
    json: 'dist/json/',
    css: 'dist/css/',
    fonts: 'dist/fonts/',
    js: 'dist/js/',
    vendor: 'dist/js/vendor/',
    jsname: 'cataloglibrary.js'
};


gulp.task('clean', function () {
    return del.sync([dist.root]);
});

gulp.task('scss', function(){
    return gulp.src(src.scss + '**/*.scss')
        .pipe(plugins.sourcemaps.init())
        .pipe(plugins.sass({
            includePaths: ['styles'].concat(neat),
        }))
        .pipe(plugins.autoprefixer('last 5 version'))
        .pipe(bless())
        .pipe(gulp.dest(dist.css))
        // write sourcemaps only on src folder
        .pipe(plugins.sourcemaps.write('.'))
        .pipe(gulp.dest(src.css));
});

