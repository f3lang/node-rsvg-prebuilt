{
	"variables": {
		"GTK_Root%": "c:\\gtk",
		"conditions": [
			[
				"OS == 'mac'",
				{
					"pkg_env": "PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/opt/X11/lib/pkgconfig:/usr/local/opt/libffi/lib/pkgconfig"
				},
				{
					"pkg_env": ""
				}
			]
		]
	},
	"targets": [
		{
			"target_name": "rsvg",
			"sources": [
				"src/Rsvg.cc",
				"src/Enums.cc",
				"src/Autocrop.cc"
			],
			"include_dirs": [
				"<!(node -e \"require('nan')\")"
			],
			"variables": {
				"packages": "librsvg-2.0 cairo-pdf cairo-svg",
				"conditions": [
					[
						"OS!='win'",
						{
							"libraries": "<!(<(pkg_env) pkg-config --libs-only-l <(packages))",
							"ldflags": "<!(<(pkg_env) pkg-config --libs-only-L --libs-only-other <(packages))",
							"cflags": "<!(<(pkg_env) pkg-config --cflags <(packages))"
						},
						{
							"include_dirs": "<!(<(python) tools/include_dirs.py <(GTK_Root) <(packages))"
						}
					]
				]
			},
			"conditions": [
				[
					"OS!='mac' and OS!='win'",
					{
						"cflags": [
							"<@(cflags)",
							"-std=c++0x"
						],
						"ldflags": [
							"<@(ldflags)"
						],
						"libraries": [
							"<@(libraries)"
						]
					}
				],
				[
					"OS=='mac'",
					{
						"xcode_settings": {
							"OTHER_CFLAGS": [
								"<@(cflags)"
							],
							"OTHER_LDFLAGS": [
								"<@(ldflags)"
							]
						},
						"libraries": [
							"<@(libraries)"
						]
					}
				],
				[
					"OS=='win'",
					{
						"sources+": [
							"src/win32-math.cc"
						],
						"include_dirs": [
							"<@(include_dirs)"
						],
						"libraries": [
							'rsvg-2.0.lib',
							'glib-2.0.lib',
							'gobject-2.0.lib',
							'cairo.lib'
						],
						"msvs_settings": {
							'VCCLCompilerTool': {
								'AdditionalOptions': [
									"/EHsc"
								]
							}
						},
						"msbuild_settings": {
							"Link": {
								"AdditionalLibraryDirectories": [
									"<(GTK_Root)\\lib"
								],
								"ImageHasSafeExceptionHandlers": "false"
							}
						}
					}
				]
			]
		},
		{
			"target_name": "copy_generated_binary",
			"type": "none",
			"dependencies": [
				"rsvg"
			],
			"copies": [
				{
					"files": [
						"build/Release/rsvg.node"
					],
					"destination": "build/"
				}
			]
		}
	],
	"conditions": [
		[
			"OS=='win'",
			{
				"targets": [
					{
						"target_name": "copy_windows_natives",
						"type": "none",
						"dependencies": [
							"copy_generated_binary"
						],
						"copies": [
							{
								"files": [
									"<(GTK_Root)\\bin\\asprintf.dll",
									"<(GTK_Root)\\bin\\atk-1.0-0.dll",
									"<(GTK_Root)\\bin\\cairo.dll",
									"<(GTK_Root)\\bin\\cairo-gobject.dll",
									"<(GTK_Root)\\bin\\cogl-1.0.dll",
									"<(GTK_Root)\\bin\\cogl-pango-1.0.dll",
									"<(GTK_Root)\\bin\\cogl-path-1.0.dll",
									"<(GTK_Root)\\bin\\croco-0.6.dll",
									"<(GTK_Root)\\bin\\epoxy-0.dll",
									"<(GTK_Root)\\bin\\ffi-7.dll",
									"<(GTK_Root)\\bin\\fontconfig.dll",
									"<(GTK_Root)\\bin\\freetype.dll",
									"<(GTK_Root)\\bin\\gailutil-2.0.dll",
									"<(GTK_Root)\\bin\\gailutil-3-3.0.dll",
									"<(GTK_Root)\\bin\\gdk-3-3.0.dll",
									"<(GTK_Root)\\bin\\gdk_pixbuf-2.0-0.dll",
									"<(GTK_Root)\\bin\\gdk-win32-2.0.dll",
									"<(GTK_Root)\\bin\\gettextlib.dll",
									"<(GTK_Root)\\bin\\gettextpo.dll",
									"<(GTK_Root)\\bin\\gettextsrc.dll",
									"<(GTK_Root)\\bin\\gio-2.0.dll",
									"<(GTK_Root)\\bin\\glib-2.0.dll",
									"<(GTK_Root)\\bin\\gmodule-2.0.dll",
									"<(GTK_Root)\\bin\\gobject-2.0.dll",
									"<(GTK_Root)\\bin\\gthread-2.0.dll",
									"<(GTK_Root)\\bin\\gtk-3-3.0.dll",
									"<(GTK_Root)\\bin\\gtk-win32-2.0.dll",
									"<(GTK_Root)\\bin\\iconv.dll",
									"<(GTK_Root)\\bin\\intl.dll",
									"<(GTK_Root)\\bin\\jasper.dll",
									"<(GTK_Root)\\bin\\jpeg62.dll",
									"<(GTK_Root)\\bin\\json-glib-1.0-0.dll",
									"<(GTK_Root)\\bin\\libpng16.dll",
									"<(GTK_Root)\\bin\\libxml2.dll",
									"<(GTK_Root)\\bin\\pango-1.0.dll",
									"<(GTK_Root)\\bin\\pangocairo-1.0.dll",
									"<(GTK_Root)\\bin\\pangoft2-1.0.dll",
									"<(GTK_Root)\\bin\\pangowin32-1.0.dll",
									"<(GTK_Root)\\bin\\pkgconf-3.dll",
									"<(GTK_Root)\\bin\\rsvg-2.0.dll",
									"<(GTK_Root)\\bin\\tiff.dll",
									"<(GTK_Root)\\bin\\tiffxx.dll",
									"<(GTK_Root)\\bin\\turbojpeg.dll",
									"<(GTK_Root)\\bin\\wing-1.0-0.dll",
									"<(GTK_Root)\\bin\\zlib1.dll"
								],
								"destination": "build/"
							}
						]
					}
				]
			}
		]
	]
}
