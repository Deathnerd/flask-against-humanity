/**
 * Created by deathnerd on 6/1/15.
 */
var gulp = require('gulp');
var shell = require('gulp-shell');
var browserSync = require('browser-sync').create();

// start up the flask server
gulp.task('flask', shell.task([
        'source env/bin/activate',
        'python runserver.py server'
        ].join(' && ')
    )
);

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