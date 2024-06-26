/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * mq_posix_receive.c
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
 *     Receive a message from a message.queue. Removes the oldest message
 *     with the highest priority from the message queue referred to by
 *     the message queue descriptor.
 *
 * Arguments:
 *     mq_descriptor - message queue descriptor
 *     message - message for queue (if the queue is empty, then, by default,
 *               mq_receive() blocks until a message becomes available, or
 *               the call is interrupted by a signal handler. If the
 *               O_NONBLOCK flag is enabled for the message queue description,
 *               then the call instead fails immediately with the error EAGAIN
 *     message_length - specifies the length of the message (zero-length
 *                      messages are allowed)
 *     message_priority - specifies the priority of this message
 *
 * Return value:
 *     status - on success returns number of bytes in the received message |
 *              MQ_POSIX_ERROR with error number set to indicate the error:
 *                  EAGAIN (queue was empty, and the O_NONBLOCK flag was set
 *                          for the message queue description)
 *                  EBADF (descriptor specified in mqdes was invalid or not
 *                         opened for reading)
 *                  EINTR (call was interrupted by a signal handler)
 *                  EINVAL (call would have blocked, and abs_timeout was
 *                          invalid, either because tv_sec was less than zero,
 *                          or because tv_nsec was less than zero or greater
 *                          than 1000 million)
 *                  EMSGSIZE (message_length was less than the mq_msgsize
 *                            attribute of the message queue)
 *                  ETIMEDOUT (call timed out before a message could be
 *                             transferred)
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */
ssize_t mq_posix_receive(
    mqd_t mq_descriptor, const char * message,
    size_t message_length, unsigned int message_priority
)
{
    int status;

    if (mq_descriptor != MQ_POSIX_ERROR && message_length >= 0)
    {
        status = mq_receive(
            mq_descriptor, message, message_length, message_priority
        );
    }
    else
    {
        status = MQ_POSIX_ERROR;
    }

    return status;
}

