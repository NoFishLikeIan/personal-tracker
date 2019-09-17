from lenses import lens

is_ok = lens.Get('ok', default=0).F(lambda s: bool(int(s))).get()
