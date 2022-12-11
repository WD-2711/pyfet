def _make_cmd(self, tmpfilename, info_dict):
    cmd = [self.exe, '--location', '-o', tmpfilename, '--compressed']
    if info_dict.get('http_headers') is not None:
        for key, val in info_dict['http_headers'].items():
            cmd += ['--header', f'{key}: {val}']

    cmd += self._bool_option('--continue-at', 'continuedl', '-', '0')
    cmd += self._valueless_option('--silent', 'noprogress')
    cmd += self._valueless_option('--verbose', 'verbose')
    cmd += self._option('--limit-rate', 'ratelimit')
    retry = self._option('--retry', 'retries')
    if len(retry) == 2:
        if retry[1] in ('inf', 'infinite'):
            retry[1] = '2147483647'
        cmd += retry
    cmd += self._option('--max-filesize', 'max_filesize')
    cmd += self._option('--interface', 'source_address')
    cmd += self._option('--proxy', 'proxy')
    cmd += self._valueless_option('--insecure', 'nocheckcertificate')
    cmd += self._configuration_args()
    cmd += ['--', info_dict['url']]
    return cmd