// -*- mode: c++; indent-tabs-mode: nil; -*-
//
// Copyright (c) 2009-2012 Illumina, Inc.
//
// Permission is hereby granted, free of charge, to any person
// obtaining a copy of this software and associated documentation
// files (the "Software"), to deal in the Software without
// restriction, including without limitation the rights to use, copy,
// modify, merge, publish, distribute, sublicense, and/or sell copies
// of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be
// included in all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
// MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
// NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
// BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
// ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
// CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//
//

/// \file

/// \author Chris Saunders
///
// take care of some (mostly C99) functions not available in VS C++
//

#ifndef __COMPAT_UTIL
#define __COMPAT_UTIL


#include <string>


#ifdef _WIN32
#define snprintf _snprintf
#endif


double
compat_round(const double x);


const char*
compat_basename(const char* s);


// gets canonical name of paths *when these refere to existing items*
// returns false on error.
bool
compat_realpath(std::string& path);


#endif
