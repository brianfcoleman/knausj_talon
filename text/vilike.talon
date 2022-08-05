mark that:
	user.mark()

mark left:
	user.mark(-1)

mark right:
	user.mark(1)

mark select:
	user.mark_select()

mark select left:
	user.mark_select(-1)

mark select right:
	user.mark_select(1)

jump <user.any_alphanumeric_key>:
	user.jump(any_alphanumeric_key)

pump <user.any_alphanumeric_key>:
	user.jump_back(any_alphanumeric_key)

remove line:
	user.remove_line()