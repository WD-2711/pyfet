def upload_file(self, metadata, filename, signer=None, sign_password=None,
                filetype='sdist', pyversion='source', keystore=None):
    """
    Upload a release file to the index.

    :param metadata: A :class:`Metadata` instance defining at least a name
                        and version number for the file to be uploaded.
    :param filename: The pathname of the file to be uploaded.
    :param signer: The identifier of the signer of the file.
    :param sign_password: The passphrase for the signer's
                            private key used for signing.
    :param filetype: The type of the file being uploaded. This is the
                    distutils command which produced that file, e.g.
                    ``sdist`` or ``bdist_wheel``.
    :param pyversion: The version of Python which the release relates
                        to. For code compatible with any Python, this would
                        be ``source``, otherwise it would be e.g. ``3.2``.
    :param keystore: The path to a directory which contains the keys
                        used in signing. If not specified, the instance's
                        ``gpg_home`` attribute is used instead.
    :return: The HTTP response received from PyPI upon submission of the
            request.
    """
    self.check_credentials()
    if not os.path.exists(filename):
        raise DistlibException('not found: %s' % filename)
    metadata.validate()
    d = metadata.todict()
    sig_file = None
    if signer:
        if not self.gpg:
            logger.warning('no signing program available - not signed')
        else:
            sig_file = self.sign_file(filename, signer, sign_password,
                                        keystore)
    with open(filename, 'rb') as f:
        file_data = f.read()