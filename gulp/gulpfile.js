var gulp = require('gulp');
var sass = require('gulp-sass');
var pug = require('gulp-pug');
var browserSync = require('browser-sync').create();

// watcher
// var watch = require('gulp-watch');

gulp.task('browserSync', function() {
    browserSync.init({
        notify: false,
        proxy: 'http://127.0.0.1:8000/'
    })
})

gulp.task('pug', function() {
    return gulp.src('src/pug/templates/**/*.pug')
        .pipe(pug({
            doctype: 'html',
            pretty: false
        }))
        .pipe(gulp.dest('../static/templates/'))
        .pipe(browserSync.reload({
            stream: true
        }))
});

gulp.task('sass', function() {
    return gulp.src('src/pug/static/sass/*.sass')
        .pipe(sass())
        .pipe(gulp.dest('../static/css/'))
        .pipe(browserSync.reload({
            stream: true
        }))
});

gulp.task('css', function() {
    return gulp.src('src/pug/static/css/*.css')
        .pipe(gulp.dest('../static/css/'))
        .pipe(browserSync.reload({
            stream: true
        }))
});

gulp.task('watch', function() {
    gulp.watch('src/pug/static/sass/*.sass', gulp.series('sass'));
    gulp.watch('src/pug/templates/**/*.pug', gulp.series('pug'));
    gulp.watch('src/pug/static/css/*.css', gulp.series('css'));
    // Other watchers
});

gulp.task('default', gulp.parallel('watch', 'browserSync'))
gulp.task('build', gulp.series('sass', 'css', 'pug'))