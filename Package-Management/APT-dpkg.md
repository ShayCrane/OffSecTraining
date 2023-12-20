### Debian Package Management

</br></br>
#### APT and dpkg
</br>
**Debian Package**: a compressed archive of a software application.
</br>
**Binary Package**: (a .deb file) contains files that can be directly used (such as programs or documentation).
</br>
**Source Package**: contains the source code for the software and the instructions required for building a binary package.

</br></br>


-------


#### Kali Repositories

A standard sources.list file for a system running Kali Linux refers to one repository (kali-rolling) and the three previously mentioned components: main, contrib, and non-free.
</br>

sources.list:  located in:

/etc/apt/sources.list; etc/apt/sources.list.d/*
</br></br>
##### Main Kali repository

</br>
>deb http://http.kali.org/kalikali-rolling main contrib non-free

</br></br>

##### The Kali-Rolling Repository
</br>
*"This is the main repository for end-users. It should always contain installable and recent packages."*
</br></br>

##### The Kali-Dev Repository
</br>
Where Kali developers resolve dependency problems, as well as the place where updated packages are pushed first. Advanced users can leverage this if there's a need for an update that was released recently and that has not yet reached the main kali-rolling repo.

</br></br>
##### The Kali Linux Mirrors
</br>
(none provided in module)


--------
</br>

#### Initializing APT
</br>
Simply run the command:
</br>
>apt update
</br>
This will download the list of currently available packages, and may take some time so be sure to time this action to take place when it won't interfere.

</br></br>
--------

#### Installing Packages
</br>
*Debian's package system allows for the installation of packages* ***without*** *their dependencies.*
</br></br>

##### How to install packages with dpkg
</br>
dpkg is used directly or indirectly through APT to install packages.  Since it doesn't need an internet connection to function, it is especially great offline operation.
</br>

To install a package without dependencies, first obtain the package .deb file, then run the following command, providing the '-i' argument (--install) and the path to the .deb package file. See the example below:
</br>
> dpkg -i man-db_2.9.3-2_amd64.deb
</br>

An alternate way to do this can be done in two steps.  Since installing both unpacks and configures the package automatically, when needed it can be replaced by two seperate commands:
</br>
> dpkg --unpack man-db_2.9.3-2_amd64.deb
> dpkg --configure man-db
</br></br>
##### Common Errors
</br>
If dpkg fails to install the package, returning an error, you can use the '--force-' options.
</br>

List all '--force' options:
> dpkg --force-help

</br>

Forcibly install a package:
> dpkg -i --force-overwrite zsh_5.8-5+b1_amd64.deb
</br>

*The above command can force-fix a file collision (pkg contains file already installed by other package)*

</br></br>
#### How to install packages with APT
</br>
*APT is a much simpler to to use for package management than dpkg.*
</br></br>
Add a package with all its dependencies by running:
</br>
> apt install package

</br></br>
#### How to upgrade Kali Linux
</br>
*The best practice is to upgrade Kali at least once a week.*

</br></br>
The apt command typically requires 'sudo' permissions to successfully execute.To perform a standard upgrade, first run:
</br>
> apt update
</br>

...followed by one of the following commands:
</br>
>apt upgrade
apt-get upgrade
aptitude safe-upgrade

</br>
*These 'upgrade' commands look for installed packages that can be upgraded without removing any packages.*
</br>
```'apt-get' will refuse to install packages that were not installed beforehand, unlike 'apt' or 'aptitude'.```

</br></br>

To perform a major version upgrade, run:
</br>
>apt-full-upgrade
</br>
or
</br>
>apt-get dist-upgrade
</br>

*apt will remove obsolete packages and install new dependencies where necessary in order to complete the upgrade.*
</br></br>

-------
</br>
The 'apt-listchanges' package will alert to possible problems when initiating a package upgrade.  The info is located in /usr/share/doc/package/NEWS.Debian to avoid surprise changes that can affect other services you use.
</br></br>
--------
</br>
#### Removing Packages
</br>
With dpkg:
>dpkg --remove kali-tools-gpu
</br>

With apt:
>apt remove [package]
</br>


**How to remove all data associated with the package**
</br></br>
With dpkg:
>dpkg -P [package]

</br>
With apt:
>apt purge [package]

</br>
*This command will also remove all dependencies.*
</br></br>

---------
</br>

#### Troubleshooting problems after an upgrade
</br></br>
- Check bug reports here: https://bugs.debian.org/; https://bugs.kali.org.
</br>
- Downgrade back to a working version.
</br>
- Reinstall with 'apt-reinstall' and 'aptitude reinstall' **but never for recovery after a malicious attack**:
</br>
>apt --reinstall install postfix
</br>

- Use '--force-*' for repairing broken dependencies (see previous sections above for more details.)
</br></br>

-------
</br>
*End of document*



