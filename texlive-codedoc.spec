# revision 17630
# category Package
# catalog-ctan /macros/latex/contrib/codedoc
# catalog-date 2010-03-30 18:14:30 +0200
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-codedoc
Version:	0.3
Release:	11
Summary:	LaTeX code and documentation in LaTeX-format file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/codedoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codedoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codedoc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The CodeDoc class is an alternative to DocStrip (and others) to
produce LaTeX code along with its documentation without
departing from LaTeX's ordinary syntax. The documentation is
prepared like any other LaTeX document and the code to be
commented verbatim is simply delimited by an environment. When
an option is turned on in the class options, this code is
written to the desired file(s). The class also includes fully
customizable verbatim environments which provide the author
with separate commands to typeset the material and/or to
execute it.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/codedoc/codedoc.cls
%doc %{_texmfdistdir}/doc/latex/codedoc/CodeDoc-manual.pdf
%doc %{_texmfdistdir}/doc/latex/codedoc/CodeDoc-manual.tex
%doc %{_texmfdistdir}/doc/latex/codedoc/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3-2
+ Revision: 750332
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 718090
- texlive-codedoc
- texlive-codedoc
- texlive-codedoc
- texlive-codedoc
- texlive-codedoc

