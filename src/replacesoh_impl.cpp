#include <fstream>
#include <iostream>
#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/vector.h>
#include <nanobind/trampoline.h>
#include <string>
#include <vector>

int replaceSOH(const std::string &input_filename,
                const std::string &output_filename) {
  const std::streamsize buffer_size = 8192; // Buffer size constant

  std::ifstream input_file(input_filename, std::ios::binary);
  if (!input_file) {
    std::cerr << "Unable to open input file: " << input_filename << std::endl;
    return 1;
  }

  std::ofstream output_file(output_filename, std::ios::binary);
  if (!output_file) {
    std::cerr << "Unable to open output file: " << output_filename << std::endl;
    return 1;
  }

  std::vector<char> buffer(buffer_size);

  while (input_file.read(buffer.data(), buffer_size) ||
         input_file.gcount() > 0) {
    std::streamsize bytes_read = input_file.gcount();

    for (std::streamsize i = 0; i < bytes_read; ++i) {
      if (buffer[i] == '\x01') {
        buffer[i] = '|';
      }
    }

    output_file.write(buffer.data(), bytes_read);
  }

  input_file.close();
  output_file.close();
  return 0;
}

namespace nb = nanobind;

NB_MODULE(replacesoh_impl, m) {
  m.def("replaceSOH", &replaceSOH, nb::arg("inputFilename"),
        nb::arg("outputFilename"));
}