/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * mq_posix_unlink.c
 * Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
 *
 * full_simple_new is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * full_simple_new is distributed in the hope that it will be useful, but
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
 *     Removes the specified message queue name (message queue name is
 *     removed immediately). The queue itself is destroyed once any other
 *     processes that have the queue open close their descriptors referring
 *     to queue.
 *
 * Arguments:
 *     mq_name - message queue name
 *
 * Return value:
 *     status - on success returns 0 | MQ_POSIX_ERROR with error number
 *              set to indicate the error:
 *                  ENAMETOOLONG (name was too long)
 *                  ENOENT (there is no message queue with the given name)
 *                  EACCES (the caller does not have permission to unlink
 *                          this message queue)
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */
int mq_posix_unlink(const char * mq_name)
{
    int status;

    if (mq_name != NULL)
    {
        status = mq_unlink(mq_name);
    }
    else
    {
        status = MQ_POSIX_ERROR;
    }

    return status;
}

