# This Puppet script kills a process named killmenow using pkill

exec { 'kill_killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep -f killmenow',
}
