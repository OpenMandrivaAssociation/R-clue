%global packname  clue
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.3_43
Release:          1
Summary:          Cluster ensembles
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-43.tar.gz
Requires:         R-stats R-cluster R-graphics R-methods 
Requires:         R-e1071 R-lpSolve R-quadprog R-relations R-cluster 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-stats R-cluster R-graphics R-methods 
BuildRequires:    R-e1071 R-lpSolve R-quadprog R-relations R-cluster 

%description
CLUster Ensembles

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/po
