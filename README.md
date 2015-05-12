# lbs-mono-fedora
Mono 4 packages for Fedora

See https://copr.fedoraproject.org/coprs/tpokorra/mono

# New packages
Package                        |Notes
-------------------------------|-----
gtk-sharp3                     |Epel6 missing gtk3
monodevelop-database           |Epel6 need fix mysql-connection-net first
mysql-connector-net            |Epel6 fail build when try apply patch0
notify-sharp3                  |Epel6 missing gtk3
npgsql                         |
nuget                          |
nunit                          |
nunit25                        |

# Dependecy list
Package                        |Run with Mono 4
-------------------------------|---------------
OpenTK                         |Work from Copr, EPEL6 need fix
RepetierHost                   |Need move to 4.5 profile
avahi-sharp                    |Need fix requires avahi-libs
banshee                        |Work from Copr, EPEL6 need fix libgpod first, EPEL7 missing gnome-desktop-devel
banshee-community-extensions   |Need move to 4.5 profile
bareftp                        |Need fix version requires of mono(Gnome.Keyring)
bless                          |Need move to 4.5 profile
boo                            |Need move to 4.5 profile
cdcollect                      |Need move to 4.5 profile
dbus-sharp                     |Work from Copr
dbus-sharp-glib                |Work from Copr
docky                          |Need fix requires of ndesk-dbus-glib
gbrainy                        |Fedora package work without changes if Copr is configured
gdata-sharp                    |Work from Copr
gecko-sharp2                   |Need move to 4.5 profile
gio-sharp                      |Work from Copr
giver                          |Nedd fix avahi-sharp
gkeyfile-sharp                 |Work from Copr
gmime                          |
gnome-desktop-sharp            |Work from Copr
gnome-do                       |Need fix version requires of mono(NDesk.DBus.GLib)
gnome-guitar                   |Need move to 4.5 profile
gnome-keyring-sharp            |Need move to 4.5 profile
gnome-rdp                      |Need fix version requires of mono(Gnome.Keyring)
gnome-sharp                    |Work from Copr
gnome-subtitles                |Fedora package work without changes if Copr is configured
graphviz                       |
gsf-sharp                      |Need move to 4.5 profile
gtk-sharp-beans                |Work from Copr
gtk-sharp2                     |Work from Copr
gtksourceview-sharp            |Need move to 4.5 profile
gudev-sharp                    |Work from Copr
hyena                          |Work from Copr
keepass                        |Work from Copr for Fedora, EPEL need fixes
kimono                         |Need fix version requires of libmono-2.0.so.1
libappindicator                |
libgpod                        |Work from Copr, EPEL6 need fix missing libusbx
log4net                        |Need move to 4.5 profile
mono-addins                    |Work from Copr
mono-basic                     |
mono-bouncycastle              |
mono-cecil                     |Work from Copr
mono-cecil-flowanalysis        |
mono-debugger                  |
mono-reflection                |
mono-tools                     |
mono-zeroconf                  |Work from Copr
monobristol                    |
monodevelop                    |Work from Copr
monodevelop-debugger-gdb       |
monosim                        |
nant                           |
ndesk-dbus                     |Work from Copr
ndesk-dbus-glib                |Work from Copr
nini                           |Need move to 4.5 profile
notify-sharp                   |Work from Copr
pdfmod                         |Need poppler-sharp
pinta                          |Fedora package work without changes if Copr is configured
poppler-sharp                  |Work from Copr
python-elasticsearch           |
qyoto                          |Need move to 4.5 profile
rescene                        |
shogun                         |
sparkleshare                   |Fedora package work without changes if Copr is configured
syntastic                      |
taglib-sharp                   |Work from Copr
themonospot-base               |
themonospot-console            |
themonospot-gui-gtk            |
themonospot-gui-qt             |
themonospot-plugin-avi         |
themonospot-plugin-mkv         |
thrift                         |
tomboy                         |Work from Copr
uwsgi                          |
webkit-sharp                   |Work from Copr
xsp                            |Work from Copr, EPEL6 need fix
