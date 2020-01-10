/*
 * Copyright © 2009 Christian Persch
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#if !defined (__TERMINAL_TERMINAL_H_INSIDE__) && !defined (TERMINAL_COMPILATION)
#error "Only <terminal/terminal.h> can be included directly."
#endif

#ifndef TERMINAL_VERSION_H
#define TERMINAL_VERSION_H

#define TERMINAL_MAJOR_VERSION (3)
#define TERMINAL_MINOR_VERSION (28)
#define TERMINAL_MICRO_VERSION (2)

#define TERMINAL_CHECK_VERSION(major,minor,micro) \
  (TERMINAL_MAJOR_VERSION > (major) || \
   (TERMINAL_MAJOR_VERSION == (major) && TERMINAL_MINOR_VERSION > (minor)) || \
   (TERMINAL_MAJOR_VERSION == (major) && TERMINAL_MINOR_VERSION == (minor) && TERMINAL_MICRO_VERSION >= (micro)))

#endif /* !TERMINAL_VERSION_H */
