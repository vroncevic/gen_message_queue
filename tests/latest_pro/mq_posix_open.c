/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * mq_posix_open.c
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
 *     Creates a new POSIX message queue or opens an existing queue.
 *     Queue is identified by name.
 *
 * Arguments:
 *     mq_name - message queue name
 *     operation_flag - argument specifies flags that control the operation
 *                      of the call (definitions of the flags values can be
 *                      obtained by including <fcntl.h>) exactly one of the
 *                      following must be specified in operation_flag:
 *                          O_RDONLY (open the queue to receive messages only)
 *                          O_WRONLY (open the queue to send messages only)
 *                          O_RDWR (open queue to both send/receive messages)
 *                      zero or more of following flags can additionally
 *                      be ORed in operation_flag:
 *                          O_CLOEXEC (set the close-on-exec flag for the
 *                                     message queue descriptor)
 *                          O_CREAT (create the message queue if it does not
 *                                   exist, owner (user ID) of the message
 *                                   queue is set to the effective user ID of
 *                                   the calling process, group ownership
 *                                   (group ID) is set to the effective group
 *                                   ID of the calling process)
 *                          O_EXCL (if O_CREAT was specified in operation_flag,
 *                                  and a queue with the given name already
 *                                  exists, then fail with the error EEXIST)
 *                          O_NONBLOCK (open the queue in nonblocking mode, in
 *                                      circumstances where mq_receive(3) and
 *                                      mq_send(3) would normally block, these
 *                                      functions instead fail with the error
 *                                      EAGAIN)
 *
 * Return value:
 *     status - on success returns message queue descriptor for use |
 *              MQ_POSIX_ERROR with error number set to indicate the error:
 *                  EACCES (queue exists, but the caller does not have
 *                          permission to open it in the specified mode)
 *                  EACCES (name contained more than one slash)
 *                  EEXIST (both O_CREAT and O_EXCL were specified in
 *                          operation_flag, but a queue with this name
 *                          already exists)
 *                  EINVAL (name doesn't follow the format in mq_overview(7))
 *                  EINVAL (O_CREAT was specified in operation_flag, and
 *                         attr was not NULL, but attr->mq_maxmsg or
 *                         attr->mq_msqsize was invalid, both of these fields
 *                         must be greater than zero, in a process that is
 *                         unprivileged (does not have the CAP_SYS_RESOURCE
 *                         capability), attr->mq_maxmsg must be less than or
 *                         equal to the msg_max limit, and attr->mq_msgsize
 *                         must be less than or equal to the msgsize_max limit
 *                         in addition, even in a privileged process,
 *                         attr->mq_maxmsg cannot exceed the HARD_MAX limit)
 *                  EMFILE (per-process limit on the number of open file and
 *                          message queue descriptors has been reached (see
 *                          description of RLIMIT_NOFILE in getrlimit(2)))
 *                  ENAMETOOLONG (name was too long)
 *                  ENFILE (system-wide limit on the total number of open
 *                          files and message queues has been reached)
 *                  ENOENT (O_CREAT flag was not specified in operation_flag,
 *                          and no queue with this name exists)
 *                  ENOENT (name was just "/" followed by no other characters)
 *                  ENOMEM (insufficient memory)
 *                  ENOSPC (insufficient space for the creation of a new
 *                          message queue, this probably occurred because
 *                          the queues_max limit was encountered)
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */
mqd_t mq_posix_open(const char * name, int operation_flag)
{
    mqd_t mq_descriptor;

    if (name != NULL && operation_flag >= 0)
    {
        mq_descriptor = mq_open(name, operation_flag);
    }
    else
    {
        mqd_t = MQ_POSIX_ERROR;
    }

    return mq_descriptor;
}

