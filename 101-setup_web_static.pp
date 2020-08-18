#This pupppet scripts assure an nginx installation

exec { '/usr/bin/env apt-get -y update':}
->package {'nginx':
ensure => installed,
}

->file { [ '/data/',
  '/data/web_static/',
  '/data/web_static/releases/',
  '/data/web_static/releases/test/',
  '/data/web_static/shared/', ]:
  ensure => directory,
}

->file {'/data/web_static/releases/test/index.html':
  ensure  => present,
  content => "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>",
}

-> exec {'/usr/bin/env ln -sf /data/web_static/releases/test/ /data/web_static/current':}
-> exec {'/usr/bin/env chown -R ubuntu:ubuntu /data/':}

->file_line {'add protocol':
ensure => present,
path   => '/etc/nginx/sites-available/default',
after  => 'listen 80 default_server;',
line   => 'location /hbnb_static/ { alias /data/web_static/current/; autoindex off;}',
}

->service { 'nginx':
ensure     => running,
}
