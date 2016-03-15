%define   _dist_ver %(sh /usr/lib/rpm/redhat/dist.sh)

Summary: Generic-purpose lossless compression algorithm by Google
Name: brotli
Version: 0.3.0
Release: 1%{?dist}
URL: https://github.com/google/brotli

Source0: https://github.com/google/brotli/archive/v%{version}.tar.gz#/brotli-v%{version}.tar.gz

License: MIT

%if "%{_dist_ver}" == ".el6"
BuildRequires: scl-utils-build
BuildRequires: devtoolset-3-gcc-c++
%endif

%description
Brotli is a generic-purpose lossless compression algorithm that compresses data using a combination of a modern variant of the LZ77 algorithm, Huffman coding and 2nd order context modeling, with a compression ratio comparable to the best currently available general-purpose compression methods. It is similar in speed with deflate but offers more dense compression.

The specification of the Brotli Compressed Data Format is defined in the following internet draft: http://www.ietf.org/id/draft-alakuijala-brotli


%prep
%setup -q

%build

%if "%{_dist_ver}" == ".el6"

scl enable devtoolset-3 'make -C tools'

%else

make -C tools

%endif

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 -p tools/bro $RPM_BUILD_ROOT%{_bindir}/bro

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{_bindir}/bro

%changelog
* Wed Mar 16 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 0.3.0-1
- 0.3.0
