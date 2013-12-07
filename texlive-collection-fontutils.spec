# revision 30396
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-fontutils
Epoch:		1
Version:	20131013
Release:	3
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
Manipulating OpenType, TrueType, Type 1,and for manipulation of
PostScript and other image formats.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
