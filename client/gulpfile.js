/**
 * Created by deathnerd on 6/1/15.
 */
var gulp = require('gulp');
var browserSync = require('browser-sync').create();

// start the browserSync instance
gulp.task('browserSync', function(){
    browserSync.init({
        proxy: "127.0.0.1:5000",
        files: [
            "humanity/templates/**",
            "static/assets/**"
        ]
    })
});