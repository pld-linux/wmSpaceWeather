CFLAGS	= $(OPTCFLAGS) -Wall
LDFLAGS	=
LIBS	= -lXpm -lX11 -lXext
DESTDIR	=
PREFIX	= /usr
BINDIR	= $(PREFIX)/bin
DATADIR	= $(PREFIX)/share
MANDIR	= $(DATADIR)/man
MAN1DIR	= $(MANDIR)/man1
DOCKLETDIR = $(DATADIR)/applications/docklets

EXTRACLEAN =
EXTRABIN =
MAN1FILE =
DOCKLETFILE =

include Makefile.include

all: $(NAME)

%.o:	%.c
	$(CC) $(CFLAGS) -c $< -o $@

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^ $(LIBS)

clean:
	rm -f $(OBJS) $(NAME) $(EXTRACLEAN)

install: $(NAME)
	install -d $(DESTDIR)$(BINDIR) $(DESTDIR)$(MAN1DIR) $(DESTDIR)$(DOCKLETDIR)
	install -m 755 $(NAME) $(DESTDIR)$(BINDIR)
	[ -z "$(EXTRABIN)" ] || install -m 755 $(EXTRABIN) $(DESTDIR)$(BINDIR)
	[ -z "$(MAN1FILE)" ] || install -m 644 $(MAN1FILE) $(DESTDIR)$(MAN1DIR)
	[ -z "$(DOCKLETFILE)" ] || install -m 644 $(DOCKLETFILE) $(DESTDIR)$(DOCKLETDIR)/$(NAME).desktop
