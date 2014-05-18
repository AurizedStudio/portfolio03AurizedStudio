module.exports = function (grunt) {
 
grunt.loadNpmTasks('grunt-contrib-connect');
grunt.loadNpmTasks('grunt-contrib-sass');
grunt.loadNpmTasks('grunt-autoprefixer');
grunt.loadNpmTasks('grunt-contrib-watch');
grunt.loadNpmTasks('grunt-browser-sync');
grunt.loadNpmTasks('grunt-stylestats');
 
grunt.initConfig({
	connect: {
		uses_defaults: {}
	},
	sass: {
		options: {
			style: 'expanded'
		},
		dist: {
			src: 'scss/style.scss',
			dest: 'htdocs/css/style.css'
		}
	},
	autoprefixer: {
		options: {
			browsers: ['last 2 version', 'ie 8', 'ie 9']
		},
		no_dest:{
			src: 'htdocs/css/style.css',
		}
	},
	imageoptim: {
		options: {
			imageAlpha: false,
			jpegMini: false,
			quitAfter: true
		},
		src: 'htdocs/img/'
	},
	watch: {
//		img: {
//			files: 'htdocs/img/*.png',
//			tasks: ['imageoptim']
//		},
		html: {
			files: ['htdocs/index.html', 'htdocs/img/*.*', 'htdocs/js/*.*'],
			options: {
				livereload: false,
			}
		},
		sass: {
			files: 'scss/*.scss',
			tasks: ['sass'],
			options: {
				livereload: false,
			}
		},
		css: {
			files: 'htdocs/css/*.css',
			tasks: ['autoprefixer']
		}
	},
	browserSync: {
		default_options: {
			files: {
				src: [
					'htdocs/*.html',
					'htdocs/css/*.css',
				]
			},
			options: {
				watchTask: true,
				proxy: "192.168.0.5:8000"
//				proxy: "192.168.24.53:8000"
			}
		}
	},
	stylestats: {
		src: ['htdocs/css/style.css']
	}
});

grunt.registerTask('default', ['connect', 'browserSync', 'watch']);
grunt.registerTask('imgbuild', ['imageoptim']);
grunt.registerTask('stats', ['stylestats']);
 
};
