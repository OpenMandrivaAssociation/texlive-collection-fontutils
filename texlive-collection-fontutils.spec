# revision 25704
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-fontutils
Epoch:		1
Version:	20120327
Release:	1
Summary:	Graphics and font utilities
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-fontutils.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-accfonts
Requires:	texlive-afm2pl
Requires:	texlive-dosepsbin
Requires:	texlive-epstopdf
Requires:	texlive-fontware
Requires:	texlive-lcdftypetools
Requires:	texlive-ps2pkm
Requires:	texlive-pstools
Requires:	psutils
Requires:	texlive-dvipsconfig
Requires:	texlive-fontinst
Requires:	texlive-fontools
Requires:	texlive-mf2pt1
Requires:	texlive-ttfutils

%description
Programs for conversion between font formats, testing fonts,
virtual fonts, .gf and .pk manipulation, mft, fontinst, etc.
Manipulating OpenType, TrueType, PostScript Type 1, and
PostScript and other images.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120327-1
+ Revision: 787847
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780296
- Update to latest release.
- Import texlive-collection-fontutils
- Import texlive-collection-fontutils

