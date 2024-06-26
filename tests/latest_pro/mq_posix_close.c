/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * mq_posix_close.c
 * Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
 *
 * latest_pro is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * latest_pro is distributed in the hope that it will be useful, but
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
 *     Closes the message queue descriptor mqdes. If the calling process
 *     has attached a notification request (see (mq_notify(3)) to this
 *     message queue via mqdes, then this request is removed, and another
 *     process can now attach a notification request.
 *
 * Arguments:
 *     mq_descriptor - message queue descriptor
 *
 * Return value:
 *     status - on success returns 0 | MQ_POSIX_ERROR with error number
 *              set to indicate the error:
 *                  EBADF (message queue descriptor specified is invalid)
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */

int mq_posix_close(mqd_t mq_descriptor)
{
    int status;

    if (mq_descriptor >= 0)
    {
        status = mq_close(mq_descriptor);
    }
    else
    {
        status = MQ_POSIX_ERROR;
    }

    return status;
}

