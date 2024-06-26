/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * mq_posix_fatal_error.c
 * Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
 *
 * simple_write is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * simple_write is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */

#include "mq_posix.h"

/**
 * Description:
 *     Print fatal error message and exit with status 1.
 *
 * Arguments:
 *     message - fatal error message
 *
 * Return value:
 *     none
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */
void mq_posix_fatal_error(const char * message)
{
    perror(message);

    exit(1);
}

